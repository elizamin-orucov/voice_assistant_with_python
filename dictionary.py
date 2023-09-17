from datetime import datetime


words = {
    "can you hear me": "Yes, I can hear you",
    "how are you": "I am fine and you",
    "i am also good": "Great",
    "thank you": "You are welcome",
    "what are you doing": "I'm learning new things",
    "what is your name": "I'm an app, I don't have a name.",
    "hi": "Hello Sir",
    "hello": "Hi sir",
    "what time is it": datetime.now().strftime('%H:%M')
}
