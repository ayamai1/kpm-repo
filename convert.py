import json

with open("store.json", "r", encoding="utf-8") as f:
    data = json.load(f)

output = []

for id, plugin in data.items():
    print(id, plugin)
    p = {
        "id": id,
        "name": plugin.get("name", None),
        "version": plugin.get("version", None),
        "icon": plugin.get("icon", ""),
        "description": plugin.get("description", None),
        "link": plugin.get("url", None),
        "hash": plugin.get("hash", None),
        "app_version": plugin.get(
            "app_version", f">={plugin.get('min_version', '11.12.0')}"
        ),
    }

    output.append(p)

with open("plugins.json", "w", encoding="utf-8") as f:
    json.dump({"plugins": output}, f, indent=2, ensure_ascii=False)
