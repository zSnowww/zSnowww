import sys
from urllib.parse import urlencode, quote

# Uso: python3 scripts/build_readme.py [BASE] > README.md
# Cambia BASE cuando FluxStats pase a tu dominio propio.
BASE = sys.argv[1] if len(sys.argv) > 1 else "https://fluxstats-beta.vercel.app"
USER = "zSnowww"
# Paleta del README: tema ryoku de FluxStats con el carmesí del dossier.
STYLE = {"theme": "ryoku", "accent_color": "e2342a"}

def url(path, **params):
    q = {**{k: v for k, v in params.items() if v is not None}, **STYLE}
    return f"{BASE}{path}?" + urlencode(q, quote_via=quote, safe="@~$")

def divider(label=None):
    return f'<p align="center"><img src="{url("/api/decor/divider", label=label, width=840)}" width="100%" alt=""></p>'

def badge(href, icon, label, value=None):
    return f'<a href="{href}"><img src="{url("/api/decor/badge", icon=icon, label=label, value=value)}" alt="{label}{": " + value if value else ""}"></a>'

terminal = url(
    "/api/decor/terminal",
    prompt="zsnow@arch ~ $",
    title="zsh — zsnow.dev",
    width=760,
    lines=";".join([
        "Backend & systems developer",
        "High-concurrency APIs with FastAPI",
        "Local-first apps with Tauri + Rust",
        "Telegram automation over MTProto",
    ]),
)

readme = f"""<div align="center">

<img src="{terminal}" width="760" alt="zsnow@arch ~ $ Backend &amp; systems developer · High-concurrency APIs · Local-first apps · Telegram automation">

<p>
  <strong>力と設計のために</strong> &middot; <em>For the sake of power and clean architecture.</em>
</p>

<p>
  Backend Developer &amp; Systems Engineering Student based in Lima, Perú 🇵🇪.<br>
  Crafting high-concurrency APIs, local-first applications, and intelligent automation systems.
</p>

{badge("https://zsnow.dev", "globe", "Web", "zsnow.dev")}&nbsp;
{badge("https://t.me/zsnow_7", "telegram", "Telegram", "@zsnow_7")}&nbsp;
{badge("https://instagram.com/veraaab_", "instagram", "Instagram", "@veraaab_")}

</div>

{divider("電脳調書")}

## `$ fastfetch --profile dossier` &middot; 電脳調書

<p align="center">
  <img src="assets/whoami-ryoku.svg" width="960" alt="System dossier de Manu (zSnow) con estética Ryoku Arch">
</p>

{divider("技術構成")}

## `$ cat /etc/ryoku/tech-stack.yaml` &middot; 技術構成

<div align="center">

<table>
  <thead>
    <tr>
      <th colspan="2" align="left">
        <code>zsnow@arch:~$ cat /etc/ryoku/tech-stack.yaml &nbsp;·&nbsp; status: 稼働中</code>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="50%" valign="top">
        <code>├─ ⚙ backend_systems:</code><br><br>
        <img src="https://skillicons.dev/icons?i=fastapi,python,rust,nodejs,ts" alt="FastAPI, Python, Rust, Node.js, TypeScript">
      </td>
      <td width="50%" valign="top">
        <code>├─ 🖥️ desktop_localfirst:</code><br><br>
        <img src="https://skillicons.dev/icons?i=tauri,react,nextjs,vite" alt="Tauri, React, Next.js, Vite">
      </td>
    </tr>
    <tr>
      <td valign="top">
        <code>├─ ▣ databases_cache:</code><br><br>
        <img src="https://skillicons.dev/icons?i=postgres,redis,supabase,mongodb" alt="PostgreSQL, Redis, Supabase, MongoDB">
      </td>
      <td valign="top">
        <code>╰─ ☁ infrastructure_ops:</code><br><br>
        <img src="https://skillicons.dev/icons?i=docker,linux,nginx,githubactions" alt="Docker, Linux, Nginx, GitHub Actions">
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2">
        <code>env: production&nbsp;&nbsp;·&nbsp;&nbsp;runtime: archlinux-zen&nbsp;&nbsp;·&nbsp;&nbsp;zen: 力と美のために</code>
      </td>
    </tr>
  </tfoot>
</table>

</div>

{divider("主要プロジェクト")}

## `$ cat /var/projects/dossier.md` &middot; 主要プロジェクト

<table>
  <thead>
    <tr>
      <th colspan="2" align="left"><code>zsnow:~$ list-projects --status featured &nbsp;·&nbsp; 選抜プロジェクト</code></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="50%" valign="top">
        <h3>🚀 <a href="https://aether.zsnow.dev">Aether OS</a> &middot; <code>個人システム</code></h3>
        <p>Sistema personal <strong>Local-First</strong> para operaciones, finanzas e infraestructura; disponible como aplicación web y de escritorio.</p>
        <img src="https://skillicons.dev/icons?i=react,ts,tauri,supabase" alt="React, TypeScript, Tauri, Supabase"><br><br>
        🌐 <a href="https://aether.zsnow.dev"><strong>aether.zsnow.dev</strong></a>
      </td>
      <td width="50%" valign="top">
        <h3>📱 <a href="https://github.com/zSnowww/AetherRelay">Aether Relay</a> &middot; <code>画面ミラー</code></h3>
        <p>Aplicación de escritorio multiplataforma para reflejar pantalla de Android con baja latencia y control físico de teclado y ratón.</p>
        <img src="https://skillicons.dev/icons?i=tauri,rust,nextjs,react" alt="Tauri, Rust, Next.js, React"><br><br>
        📦 <a href="https://github.com/zSnowww/AetherRelay"><strong>GitHub Repo</strong></a> &middot; <a href="https://github.com/zSnowww/AetherRelay/releases"><strong>Releases</strong></a>
      </td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td colspan="2"><code>ポートフォリオ詳細: <a href="https://zsnow.dev/#proyectos">https://zsnow.dev/#proyectos</a></code></td>
    </tr>
  </tfoot>
</table>

{divider("開発統計")}

## `$ github-activity --stats` &middot; 開発統計

<p align="center">
  <img src="{url("/api/github/profile", username=USER)}" width="720" alt="GitHub stats, top languages and contribution streak for {USER}">
</p>

<p align="center">
  <img src="{url("/api/github/contributions", username=USER, type="activity", width=720, hide_stats="true")}" width="720" alt="Weekly contribution activity for the past year">
</p>

{divider("雪")}

<div align="center">
<sub>力と美のために &middot; Crafted with discipline, code &amp; paper-ink aesthetics by Manu (zSnow) &middot; @zSnowww<br>
Cards by <a href="{BASE}">FluxStats</a></sub>
</div>
"""
print(readme, end="")
