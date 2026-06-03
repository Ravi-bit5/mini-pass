from fastapi import APIRouter

router = APIRouter()


@router.get("/repositories")
def get_repositories():
    return [
        {
            "name": "mini-pass",
            "url": "https://github.com/Ravi-bit5/mini-pass"
        },
        {
            "name": "portfolio",
            "url": "https://github.com/Ravi-bit5/portfolio"
        },
        {
            "name": "blog-app",
            "url": "https://github.com/Ravi-bit5/blog-app"
        }
    ]