<code><a href="https://github.com/umarurize/U_World_Border"><img height="25" src="./logo/logo.jpg" alt="U-World-Border" /></a>&nbsp;U-World-Border</code>

![Total Git clones](https://img.shields.io/badge/dynamic/json?label=Total%20Git%20clones&query=$&url=https://cdn.jsdelivr.net/gh/umarurize/U_World_Border@master/clone_count.txt&color=brightgreen)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/umarurize/U_World_Border/total)
![](https://img.shields.io/badge/language-python-blue.svg) 
[![GitHub License](https://img.shields.io/github/license/umarurize/U_World_Border)](LICENSE)

***

### ✨Introductions
* **Different dimensions' world borders can be independently configured**
* **Free of tedious file editing**
* **Support with full GUI forms**
* **Support with hot reloading**
* **Support with localized multi-language**

***

### 📦Installation
<details>
<summary>Check your Endstone's version</summary>

* **Endstone 0.9.0+**
  * 251229

</details>

<details>
<summary>Check your pre-plugins</summary>

* **Optional pre-plugin**
  * [ZX_UI](https://www.minebbs.com/resources/zx-ui.9830/)

</details>

1. Ensure you have downloaded the correct version and installed all required pre-plugins
2. Place the `.whl` file into your server's `plugins` folder
3. Restart your server
4. Enter the command `/ubd` to call out the main form of U-World-Border

***

### 📄File structure
```
plugins/
├─ u-world-border/
│  ├─ config.json
│  ├─ lang/
│  │  ├─ zh_CN.json
│  │  ├─ en_US.json
```

***

### ⚙️Configuration
`config.json`

```json5
{
    "overworld": {
        "is_enabled": false,  // If set to true, this dimension's world border will be enabled.
        "center_pos": [0, 0], // [x, z],
        "radius": 10000
    },
    "nether": {
        "is_enabled": false,
        "center_pos": [0, 0],
        "radius": 10000
    },
    "theend": {
        "is_enabled": false,
        "center_pos": [0, 0],
        "radius": 10000
    }
}
```
***

### 🌎Localized multi-language
* Currently supported localized languages for U-World-Border:
- [x] `zh_CN`
- [x] `en_US`
* How to add more languages to U-World-Border? Here we use Japanese for an example.
  * Create a file named `ja_JP.json` and place it into `lang` folder
  * Copy all key-value pairs from `en_US.json` and paste them into `ja_JP.json`
  * Refer to the English values and translate them all into Japanese, then save the file.
  * Restart your server, and you're all done!
* If you'd like your translated language to be included as one of the official languages of this plugin, feel free to shoot over a PR.

***

### 🎨Screenshots
You can view related screenshots of U-World-Border from images folder of this repo.
