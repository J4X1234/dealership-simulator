# Car Dealership Simulator
This is a Python program that simulates a basic car dealership system where users can buy, sell, and paint cars. Each car has a name, color, and price, and the user manages a virtual bank account to perform transactions. The program uses a simple terminal-based menu and supports saving/loading car inventory from .txt files.

## Features
View current bank account balance

Buy new cars and apply an automatic markup

Sell cars from your inventory

Paint/repaint existing cars

Save and load car inventories using text files

## Key Concepts Used
Object-Oriented Programming
The program uses a separate Car class to encapsulate car attributes and behaviors, like painting.

File I/O
Reads and writes inventory data and bank balance to plain text files for persistent storage.

Control Flow & User Input
Uses while loops, conditionals, and input() to guide user choices through a menu-driven interface.

Global State Management
Tracks bank account balance and car inventory throughout the session.

Basic Simulation Logic
Applies a 20% markup to newly purchased cars and updates values in real-time during sales or edits.
