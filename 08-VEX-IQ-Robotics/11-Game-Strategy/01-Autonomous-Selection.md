# 🎯 Lesson 1: Multi-Slot Autonomous (The Playbook)

In a competition, your partner might start on the left side or the right side. You need different "Plays." Instead of downloading new code, you build a **Menu** on the Brain screen to choose your play before the match starts.

## 1. The 5-Year-Old Spark ⚡
It's like a video game character select screen. Before the game starts, you tap the screen to pick "Play A" (The Aggressive Play) or "Play B" (The Defensive Play).

## 2. The Deep Dive 🤿
We use a variable called `selected_play` and a simple UI button to cycle through options.

```python
selected_play = 1

def choose_play():
    global selected_play
    if brain.screen.pressing():
        selected_play += 1
        if selected_play > 3: selected_play = 1
        brain.screen.clear_screen()
        brain.screen.print("SELECTED PLAY: " + str(selected_play))
        wait(200, MSEC)

# In Autonomous, we use an IF to run the right code
def user_autonomous():
    if selected_play == 1:
        # Strategy: Score in the high goal
        pass
    elif selected_play == 2:
        # Strategy: Clear the corner
        pass
```

## 3. The Quest: The Playbook ⚔️
1. Create `01_playbook_task.py`.
2. Create 3 different autonomous routines: `Short`, `Medium`, and `Long`.
3. Use the Brain's Up/Down buttons to toggle between them.
4. Display the name of the active play in BIG letters on the screen.
