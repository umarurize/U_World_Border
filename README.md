# U-World-Border

<code><a href="https://github.com/umarurize/U_World_Border"><img height="25" src="./logo/logo.jpg" alt="U-World-Border" /></a>&nbsp;U-World-Border</code>

## Introductions
* **3 types of dimensions' world borders can be independently set**
  * Overworld
  * Nether
  * The End
* **Full GUI forms**
* **Hot reload support**
* **Localized languages support**

## Installation
<details>
<summary>Check your Endstone's version</summary>

* **Endstone 0.9.0+**
  * 251229

</details>

<details>
<summary>Check pre-plugins</summary>

* **[ZX_UI]()**


</details>

Put `.whl` file into the endstone plugins folder, and then start the server. Enter the command `/ubd` to call out the main form.

## File structure
```
Plugins/
├─ u-world-border/
│  ├─ config.json
│  ├─ lang/
│  │  ├─ zh_CN.json
│  │  ├─ en_US.json
```

## Configuration
U-World-Border allows operators to edit/update `config.json` through GUI forms with ease, here are just simple explanations for relevant configurations.

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

## Languages
- [x] `zh_CN`
- [x] `en_US`

Of course, you can add your mother language to U-World-Border, just create `XX_XX.json` (such as `ja_JP.json`) and translate value with reference to `en_US.json`.

You can also create a PR to this repo to make your mother language one of the official languages of U-World-Border.

## Screenshots
You can view related screenshots of U-World-Border from images folder of this repo.


![Total Git clones](https://img.shields.io/badge/dynamic/json?label=Total%20Git%20clones&query=$&url=https://cdn.jsdelivr.net/gh/umarurize/U_World_Border@master/clone_count.txt&color=brightgreen)
![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/umarurize/U_World_Border/total)
![](https://img.shields.io/badge/language-python-blue.svg) 
[![GitHub License](https://img.shields.io/github/license/umarurize/U_World_Border)](LICENSE)
