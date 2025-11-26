package com.example.chatbot

import org.springframework.http.HttpEntity
import org.springframework.http.HttpHeaders
import org.springframework.http.MediaType
import org.springframework.web.bind.annotation.*
import org.springframework.web.client.RestTemplate

@RestController
class ChatController {

    private val restTemplate = RestTemplate()
    // Using 8000 for Python Server
    private val pythonBotUrl = "http://localhost:8000/chat"

    data class ChatRequest(val message: String, val user_id: Int = 1)
    data class ChatResponse(val response: String)

    @PostMapping("/chat")
    fun chat(@RequestBody request: ChatRequest): ChatResponse {
        val headers = HttpHeaders().apply { contentType = MediaType.APPLICATION_JSON }

        val entity = HttpEntity(request, headers)

        try {
            val pythonResponseMap = restTemplate.postForObject(
                pythonBotUrl,
                entity,
                Map::class.java
            ) as Map<*, *>

            val replyText = pythonResponseMap["response"]?.toString()

            if (replyText.isNullOrEmpty()) {
                return ChatResponse("Error: Received empty response from Python server.")
            }

            return ChatResponse(replyText)

        } catch (e: Exception) {
            println("Error calling Python server: ${e.message}")
            return ChatResponse("Internal Server Error: Failed to connect to Python LLM service.")
        }
    }
}