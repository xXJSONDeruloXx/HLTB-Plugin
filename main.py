import quart
from quart import Quart, request, jsonify
from quart_cors import cors
from howlongtobeatpy import HowLongToBeat

app = Quart(__name__)
app = cors(app, allow_origin="https://chat.openai.com")

@app.post("/game_info/<string:game_name>")
async def get_game_info(game_name: str):
    hltb = HowLongToBeat()
    results = await hltb.async_search(game_name)
    if results is None or len(results) == 0:
        return jsonify({"error": "No results found for this game name"}), 404
    game_info = {
            "game_id": results[0].game_id,
            "game_name": results[0].game_name,
            "game_alias": results[0].game_alias,
            "game_type": results[0].game_type,
            "game_image_url": results[0].game_image_url,
            "game_web_link": results[0].game_web_link,
            "review_score": results[0].review_score,
            "profile_dev": results[0].profile_dev,
            "profile_platforms": results[0].profile_platforms,
            "release_world": results[0].release_world,
            "main_story": results[0].main_story,
            "main_extra": results[0].main_extra,
            "completionist": results[0].completionist,
            "all_styles": results[0].all_styles,
            "similarity": results[0].similarity
        }
    return jsonify(game_info)

# paths for manifest, do not touch
@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
