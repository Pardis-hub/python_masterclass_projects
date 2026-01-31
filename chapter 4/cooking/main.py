from sanic import Sanic
from sanic.response import json, text
from pydantic import BaseModel
from typing import List, Optional
import uuid
import csv
import io

app = Sanic("RecipeAPI")

recipes = []

class RecipeModel(BaseModel):
    title: str
    category: str
    description: str
    estimated_time: int
    difficulty: Optional[str] = None
    ingredients: Optional[List[str]] = None


@app.post("/recipes")
async def create_recipe(request):
    try:
        data = RecipeModel(**request.json)
    except Exception as e:
        return json({"error": str(e)}, status=400)

    recipe = data.dict()
    recipe["id"] = str(uuid.uuid4())
    recipes.append(recipe)
    return json(recipe, status=201)


@app.get("/recipes")
async def get_recipes(request):
    return json(recipes)


@app.get("/recipes/<recipe_id>")
async def get_recipe(request, recipe_id):
    for r in recipes:
        if r["id"] == recipe_id:
            return json(r)
    return json({"error": "Recipe not found"}, status=404)


@app.put("/recipes/<recipe_id>")
async def update_recipe(request, recipe_id):
    for r in recipes:
        if r["id"] == recipe_id:
            try:
                data = RecipeModel(**request.json)
            except Exception as e:
                return json({"error": str(e)}, status=400)

            r.update(data.dict())
            return json(r)
    return json({"error": "Recipe not found"}, status=404)


@app.delete("/recipes/<recipe_id>")
async def delete_recipe(request, recipe_id):
    global recipes
    new_recipes = [r for r in recipes if r["id"] != recipe_id]
    if len(new_recipes) == len(recipes):
        return json({"error": "Recipe not found"}, status=404)
    recipes = new_recipes
    return text("", status=204)


@app.get("/recipes/export")
async def export_recipes(request, format: str = "json"):
    if format.lower() == "json":
        return json(recipes)

    elif format.lower() == "csv":
        if not recipes:
            return text("", status=204)

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=recipes[0].keys())
        writer.writeheader()
        for r in recipes:
            writer.writerow(r)
        return text(
            output.getvalue(),
            headers={
                "Content-Disposition": 'attachment; filename="recipes.csv"',
                "Content-Type": "text/csv",
            },
        )

    else:
        return json({"error": "Format not supported"}, status=400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
