#include <iostream>
#include <string>
#include <vector>
#include <curl/curl.h>
#include <nlohmann/json.hpp>
#include <mutex>
#include <thread>
#include <condition_variable>
#include <chrono>

class DiscordWebhookHandler {
public:
    DiscordWebhookHandler(const std::string& webhook_url)
        : webhook_url(webhook_url), auto_flush(true) {}

    void log(const std::string& message, const std::string& level) {
        std::lock_guard<std::mutex> lock(mtx);
        buffer.push_back(formatMessage(message, level));
        if (auto_flush) {
            send();
        }
    }

    void send() {
        std::lock_guard<std::mutex> lock(mtx);
        if (buffer.empty()) return;

        std::string log_message;
        for (const auto& msg : buffer) {
            log_message += msg + "\n";
        }

        nlohmann::json json_data;
        json_data["content"] = "```diff\n" + log_message + "```";

        CURL* curl = curl_easy_init();
        if (curl) {
            curl_easy_setopt(curl, CURLOPT_URL, webhook_url.c_str());
            curl_easy_setopt(curl, CURLOPT_POST, 1L);
            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_data.dump().c_str());
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, nullptr); // header ayarları gerekebilir
            CURLcode res = curl_easy_perform(curl);
            if (res != CURLE_OK) {
                std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
            }
            curl_easy_cleanup(curl);
        }
        buffer.clear();
    }

    private:
    std::string formatMessage(const std::string& message, const std::string& level) {
        return "[" + level + "] " + message;
    }

    std::string webhook_url;
    std::vector<std::string> buffer;
    std::mutex mtx;
    bool auto_flush;
};

int main() {
    std::string webhook_url = "YOUR_WEBHOOK_URL"; // Webhook URL'nızı buraya yazın
    DiscordWebhookHandler logger(webhook_url);

    logger.log("Program başlatıldı!", "INFO");

    // Ekstra log mesajları
    logger.log("Bu bir hata mesajıdır.", "ERROR");

    std::this_thread::sleep_for(std::chrono::seconds(1)); // Gecikme eklemek için
    return 0;
}
