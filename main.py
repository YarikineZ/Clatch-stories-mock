﻿from fastapi import FastAPI, Response

# http://127.0.0.1:8000/docs
# uvicorn main:app --reload

app = FastAPI()


@app.get("/story/")
def get_legacy_data():
    data = """
[
  {
    "id": 0,
    "progressBarColor": "000000",
    "statusBarColor": "light",
    "preview": {
      "previewImageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story1.png",
      "previewText": {
        "textColor": "000000",
        "title": "Полезная еда",
        "subTitle": "Подзаголовок в четыре слова",
        "sizeBetweenTitles": 0
      }
    },
    "storyScreens": [
      {
        "imageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story1screen1.svg",
        "duration": 15,
        "storyText": {
          "textColor": "FFFFFF",
          "title": "Экран с попугаями",
          "fontSizeTitle": 0,
          "lineSpacingTitle": 0,
          "subTitle": "На самом деле попугаи нифига не милые",
          "fontSizeSubtitle": 0,
          "lineSpacingSubtitle": 0,
          "sizeBetweenTitles": 0,
          "textPosition": "top",
          "textAlign": "center"
        }
      },
      {
        "imageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story1screen2.svg",
        "duration": 15,
        "storyText": {
          "textColor": "FFFFFF",
          "title": "Экран без Subtitle, но с кнопой",
          "fontSizeTitle": 0,
          "lineSpacingTitle": 0,
          "fontSizeSubtitle": 0,
          "lineSpacingSubtitle": 0,
          "sizeBetweenTitles": 0,
          "textPosition": "top",
          "textAlign": "left"
        },
        "storyButton": {
          "text": "Кнопка",
          "textColor": "000000",
          "buttonColor": "FFFFFF",
          "url": "https://www.youtube.com/watch?v=gke69PitnHk"
        }
      },
      {
        "imageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story1screen3.svg",
        "duration": 15,
        "storyText": {
          "textColor": "FFFFFF",
          "title": "Много текста",
          "subTitle": "Очень много текста, очень много текста, очень много текста, очень много текста, очень много текста, очень много текста, очень много текста, очень много текста, очень много текста, очень много текста",
          "fontSizeTitle": 0,
          "lineSpacingTitle": 0,
          "fontSizeSubtitle": 0,
          "lineSpacingSubtitle": 0,
          "sizeBetweenTitles": 0,
          "textPosition": "top",
          "textAlign": "left"
        },
        "storyButton": {
          "text": "Кнопка",
          "textColor": "000000",
          "buttonColor": "FFFFFF",
          "url": "https://www.youtube.com/watch?v=gke69PitnHk"
        }
      }
    ],
    "accessLevel": "allUsers"
  },
  {
    "id": 0,
    "progressBarColor": "000000",
    "statusBarColor": "light",
    "preview": {
      "previewImageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story2.png",
      "previewText": {
        "textColor": "000000",
        "title": "Полезная еда",
        "sizeBetweenTitles": 0
      }
    },
    "storyScreens": [
      {
        "imageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story2screen1.svg",
        "duration": 15,
        "storyText": {
          "textColor": "000000",
          "title": "Тексты справа",
          "subTitle": "В этом экране нет параметров с размерами",
          "textPosition": "top",
          "textAlign": "right"
        }
      },
      {
        "imageUrl": "https://raw.githubusercontent.com/YarikineZ/Clatch-stories-mock/main/assets/story2screen2.svg",
        "duration": 15,
        "storyText": {
          "textColor": "FFFFFF",
          "title": "Все еще текст справа, размеры текстов по нулям",
          "fontSizeTitle": 0,
          "lineSpacingTitle": 0,
          "fontSizeSubtitle": 0,
          "lineSpacingSubtitle": 0,
          "sizeBetweenTitles": 0,
          "textPosition": "top",
          "textAlign": "right"
        }
      }
    ],
    "accessLevel": "allUsers"
  }
]
    """
    return Response(content=data, media_type="application/json")