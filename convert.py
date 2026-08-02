import json

category_labels = {
    "library": ("Library", "key_avatar_backgroundInProfileBlue"),
    "utilities": ("Utilities", "key_avatar_background2Orange"),
    "customization": ("Customization", "key_avatar_backgroundViolet"),
    "informational": ("Informational", "key_color_lightblue"),
    "fun": ("Fun", "key_avatar_background2Cyan"),
    "messages": ("Messages", "key_avatar_backgroundGreen"),
}


def category_label(s: str):
    return category_labels.get(s.lower()) if type(s) is str else None


with open("store.json", "r", encoding="utf-8") as f:
    data = json.load(f)

output = []

for id, plugin in data.items():
    print(id)
    p = {
        "id": id,
        "name": plugin.get("name"),
        "author": plugin.get("author"),
        "version": plugin.get("version"),
        "icon": plugin.get("icon"),
        "description": plugin.get("description"),
        "link": plugin.get("url"),
        "hash": plugin.get("hash"),
        "app_version": plugin.get(
            "app_version", f">={plugin.get('min_version', '11.12.0')}"
        ),
        "tags": category_label(plugin.get("status")),
    }

    if p["tags"] is not None:
        p["tags"] = [p["tags"]]

    p = {k: v for k, v in p.items() if v is not None}

    output.append(p)

with open("plugins.json", "w", encoding="utf-8") as f:
    json.dump({"plugins": output}, f, indent=2, ensure_ascii=False)
