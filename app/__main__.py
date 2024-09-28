import uvicorn

def main():
    """ Entry point """
    uvicorn.run(
        "src.app:app",
        workers=2,
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        factory=True,
        reload=True,
    )

if __name__ == "__main__":
    main()