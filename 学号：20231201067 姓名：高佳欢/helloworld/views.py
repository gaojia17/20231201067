from django.http import Http404, HttpResponse 
from django.shortcuts import render 

# Create your views here. 
def index(request): 
    return render(request, "singlepage/index.html") 

# The texts are much longer in reality, but have 
# been shortened here to save space 
texts = [
    "Biology studies living organisms, from tiny bacteria to large whales. It explores life processes like growth, reproduction, and how organisms interact with their environments. Key areas include cell biology, genetics, and ecology, helping us understand life’s origins and sustain Earth’s biodiversity",
    "History records and analyzes past human events, from ancient civilizations (e.g., Egypt, China) to modern wars. It examines societies, cultures, and leaders, revealing patterns that shape today’s world. Studying history teaches critical thinking and helps avoid repeating past mistakes.",
    "Physics explores matter, energy, and their interactions—from atoms to the universe. It explains gravity, electricity, and light, with laws like Newton’s motion rules. Its discoveries drive tech: from smartphones (using electromagnetism) to space travel, making it fundamental to understanding the physical world."
] 

def section(request, num): 
    if 1 <= num <= 3: 
        return HttpResponse(texts[num - 1]) 
    else: 
        raise Http404("No such section")