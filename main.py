import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-course-udemy!")
    print("DEEPSEEK_API_KEY:", os.getenv("DEEPSEEK_API_KEY"))


if __name__ == "__main__":
    main()
