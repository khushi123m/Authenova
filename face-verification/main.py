from fastapi import FastAPI, UploadFile, File, HTTPException
from app.service import verify_images

app = FastAPI(
    title="Authenova Face Verification API",
    description="Face verification API using FaceNet embeddings",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Authenova Face Verification API is running"
    }


@app.post("/verify-face")
async def verify_face(
    reference_image: UploadFile = File(...),
    test_image: UploadFile = File(...)
):
    try:
        # Read uploaded images as bytes
        reference_data = await reference_image.read()
        test_data = await test_image.read()

        # Validate that files were actually uploaded
        if not reference_data:
            raise HTTPException(
                status_code=400,
                detail="Reference image is empty."
            )

        if not test_data:
            raise HTTPException(
                status_code=400,
                detail="Test image is empty."
            )

        # Verify faces
        result = verify_images(
            reference_data,
            test_data,
            threshold=0.70
        )

        return result

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Face verification failed: {str(e)}"
        )