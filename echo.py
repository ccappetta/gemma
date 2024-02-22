# This script lets you pass input and receive it as a reply. It's nice to test that your inputs and outputs are being successfully processed on the boomi side.

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No input provided")
        sys.exit(1)

    input_text = sys.argv[1]
    print(f"Received input: {input_text}")
