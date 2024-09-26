# from fastapi import FastAPI
# from pydantic import BaseModel
# from pred import output_report
# from trainedModels import load_models

# app = FastAPI()
# models=load_models()

# class CommentRequest(BaseModel):
#     input_string: str

# @app.post("/predict-comment")
# def comment_prediction(request: CommentRequest):
#     input_string = request.input_string

#     prediction_report = output_report(input_string,models)
#     # Return the prediction result
#     print(prediction_report)
#     return prediction_report




# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="127.0.0.1", port=8000)




from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Vercel"}
