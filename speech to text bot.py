import asyncio
import edge_tts
import pygame
import os

pygame.mixer.init()

async def speak(text):
    file = "voice.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-AriaNeural"
    )

    await communicate.save(file)

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(file)

while True:
    text = input("Enter text (type 'exit' to stop): ")

    if text.lower() == "exit":
        print("Program Closed.")
        break

    asyncio.run(speak(text))