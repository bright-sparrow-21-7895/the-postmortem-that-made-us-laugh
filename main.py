import os

# Entry text for "The Postmortem That Made Us Laugh" (two sentences, 107 chars).
ENTRY = (
    "Root cause: the agent deployed on Friday. "
    "Contributing factor: it was, technically, still Friday somewhere."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
