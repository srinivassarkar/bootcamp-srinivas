<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Abstract Base Class Example with Streaming</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Python Abstract Base Class Example with Streaming</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines an abstract base class called <code>Streamable</code> using the <code>abc</code> module. The class includes an abstract method <code>stream</code> that must be implemented by any subclass. The <code>VideoStream</code> and <code>AudioStream</code> classes inherit from <code>Streamable</code> and provide their own implementations of the <code>stream</code> method.</p>
        
        <h3>Why?</h3>
        <p>Abstract base classes are useful for defining a common interface for a group of related classes. They ensure that derived classes implement specific methods, promoting a consistent API and enabling polymorphism.</p>
        
        <h3>What?</h3>
        <p>The <code>Streamable</code> class serves as a blueprint for streamable content, requiring subclasses to implement the <code>stream</code> method. The <code>VideoStream</code> and <code>AudioStream</code> classes provide their own logic for streaming video and audio, respectively.</p>
        
        <h3>How?</h3>
        <p>When instances of <code>VideoStream</code> and <code>AudioStream</code> are created, their <code>stream</code> methods can be called to retrieve the respective streaming messages. This demonstrates polymorphism, as the same method name behaves differently depending on the class.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from abc import ABC, abstractmethod

class Streamable(ABC):
    @abstractmethod
    def stream(self):
        pass

class VideoStream(Streamable):
    def stream(self):
        return "Streaming video..."

class AudioStream(Streamable):
    def stream(self):
        return "Streaming audio..."

# Create instances
video = VideoStream()
audio = AudioStream()

print(video.stream())  # Output: Streaming video...
print(audio.stream())  # Output: Streaming audio...
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use abstract base classes in Python to define a common interface for different types of streamable content, allowing for polymorphism and ensuring that all derived classes implement the required methods.
    </div>

</body>
</html>