import json

with open("store.json", "r", encoding="utf-8") as f:
    data = json.load(f)

output = []

for id, plugin in data.items():
    print(id, plugin)
    p = {
        "id": id,
        "name": plugin.get("name"),
        "version": plugin.get("version"),
        "icon": plugin.get("icon"),
        "description": plugin.get("description"),
        "link": plugin.get("url"),
        "hash": plugin.get("hash"),
        "app_version": plugin.get(
            "app_version", f">={plugin.get('min_version', '11.12.0')}"
        ),
    }

    p = {k: v for k, v in p.items() if v is not None}

    output.append(p)

with open("plugins.json", "w", encoding="utf-8") as f:
    json.dump({"plugins": output}, f, indent=2, ensure_ascii=False)
