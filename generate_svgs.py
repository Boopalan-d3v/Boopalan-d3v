import os
from html import escape

def load_portrait(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = [line.rstrip() for line in f.read().splitlines()]
    return lines

def generate_svg(theme="dark"):
    is_dark = (theme == "dark")
    portrait_lines = load_portrait("portrait.txt")

    # Canvas Dimensions
    WIDTH = 1180
    HEIGHT = 610

    # Colors and Gradients
    if is_dark:
        bg_start = "#060913"
        bg_end = "#03060c"
        bg_glow = "#0e172a"
        titlebar_bg = "#0B1120"
        titlebar_opacity = "0.85"
        titlebar_border = "#1E293B"
        
        card_bg = "#0B1220"
        card_bg_opacity = "0.55"
        subcard_bg = "#070D18"
        subcard_bg_opacity = "0.75"
        
        border_grad_stops = """
          <stop offset="0%" stop-color="#7C3AED"/>
          <stop offset="50%" stop-color="#22D3EE"/>
          <stop offset="100%" stop-color="#10B981"/>
        """
        
        ascii_grad_stops = """
          <stop offset="0%" stop-color="#22D3EE">
            <animate attributeName="stop-color" values="#22D3EE;#7C3AED;#38BDF8;#22D3EE" dur="10s" repeatCount="indefinite"/>
          </stop>
          <stop offset="50%" stop-color="#38BDF8">
            <animate attributeName="stop-color" values="#38BDF8;#22D3EE;#818CF8;#38BDF8" dur="10s" repeatCount="indefinite"/>
          </stop>
          <stop offset="100%" stop-color="#818CF8">
            <animate attributeName="stop-color" values="#818CF8;#38BDF8;#7C3AED;#818CF8" dur="10s" repeatCount="indefinite"/>
          </stop>
        """
        
        text_primary = "#F8FAFC"
        text_secondary = "#E2E8F0"
        text_muted = "#94A3B8"
        text_faint = "#475569"
        
        accent_cyan = "#22D3EE"
        accent_sky = "#38BDF8"
        accent_emerald = "#10B981"
        accent_violet = "#A855F7"
        
        scanline_color = "#38BDF8"
        scanline_opacity = "0.02"
        divider_stroke = "#1E293B"
        
        badge_border = "#334155"
        badge_bg = "#1E293B"
        badge_text = "#38BDF8"
        laser_color = "#22D3EE"
        laser_opacity = "0.7"
    else:
        # Genuinely designed light theme!
        bg_start = "#F8FAFC"
        bg_end = "#F1F5F9"
        bg_glow = "#E0F2FE"
        titlebar_bg = "#FFFFFF"
        titlebar_opacity = "0.95"
        titlebar_border = "#CBD5E1"
        
        card_bg = "#FFFFFF"
        card_bg_opacity = "0.85"
        subcard_bg = "#F8FAFC"
        subcard_bg_opacity = "0.95"
        
        border_grad_stops = """
          <stop offset="0%" stop-color="#2563EB"/>
          <stop offset="50%" stop-color="#0284C7"/>
          <stop offset="100%" stop-color="#059669"/>
        """
        
        ascii_grad_stops = """
          <stop offset="0%" stop-color="#0284C7">
            <animate attributeName="stop-color" values="#0284C7;#2563EB;#7C3AED;#0284C7" dur="10s" repeatCount="indefinite"/>
          </stop>
          <stop offset="50%" stop-color="#2563EB">
            <animate attributeName="stop-color" values="#2563EB;#7C3AED;#0284C7;#2563EB" dur="10s" repeatCount="indefinite"/>
          </stop>
          <stop offset="100%" stop-color="#7C3AED">
            <animate attributeName="stop-color" values="#7C3AED;#0284C7;#2563EB;#7C3AED" dur="10s" repeatCount="indefinite"/>
          </stop>
        """
        
        text_primary = "#0F172A"
        text_secondary = "#1E293B"
        text_muted = "#475569"
        text_faint = "#94A3B8"
        
        accent_cyan = "#0284C7"
        accent_sky = "#0369A1"
        accent_emerald = "#059669"
        accent_violet = "#6D28D9"
        
        scanline_color = "#0F172A"
        scanline_opacity = "0.015"
        divider_stroke = "#E2E8F0"
        
        badge_border = "#CBD5E1"
        badge_bg = "#EFF6FF"
        badge_text = "#0369A1"
        laser_color = "#0284C7"
        laser_opacity = "0.35"

    # ASCII portrait positioning
    START_X = 69
    START_Y = 106
    LINE_HEIGHT = 7.1

    ascii_tspans = []
    y_pos = START_Y
    for line in portrait_lines:
        ascii_tspans.append(f'<tspan x="{START_X}" y="{y_pos:.2f}" xml:space="preserve">{escape(line)}</tspan>')
        y_pos += LINE_HEIGHT

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Boopalan S - Full Stack Software Engineer Profile Banner">
  <title>Boopalan S - Full Stack Software Engineer</title>
  <desc>Professional engineering hero banner for Boopalan S featuring an ASCII portrait, system telemetry, technical stack matrix, and live terminal interface.</desc>

  <defs>
    <!-- Gradients -->
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      {border_grad_stops}
    </linearGradient>

    <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      {ascii_grad_stops}
    </linearGradient>

    <radialGradient id="bgGrad" cx="50%" cy="30%" r="85%">
      <stop offset="0%" stop-color="{bg_glow}"/>
      <stop offset="50%" stop-color="{bg_start}"/>
      <stop offset="100%" stop-color="{bg_end}"/>
    </radialGradient>

    <!-- Sleek Laser Scanner Beam -->
    <linearGradient id="laserGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{laser_color}" stop-opacity="0"/>
      <stop offset="20%" stop-color="{laser_color}" stop-opacity="{laser_opacity}"/>
      <stop offset="50%" stop-color="{laser_color}" stop-opacity="0.95"/>
      <stop offset="80%" stop-color="{laser_color}" stop-opacity="{laser_opacity}"/>
      <stop offset="100%" stop-color="{laser_color}" stop-opacity="0"/>
    </linearGradient>

    <!-- Scanline Pattern -->
    <pattern id="scanlines" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="{scanline_color}" opacity="{scanline_opacity}"/>
    </pattern>

    <!-- Clip Paths for Clean Borders -->
    <clipPath id="leftCardClip">
      <rect x="20" y="64" width="446" height="526" rx="14"/>
    </clipPath>
    <clipPath id="rightCardClip">
      <rect x="484" y="64" width="676" height="526" rx="14"/>
    </clipPath>

    <!-- Portrait Reveal Mask -->
    <mask id="portraitReveal" maskUnits="userSpaceOnUse" x="0" y="0" width="{WIDTH}" height="{HEIGHT}">
      <rect x="0" y="0" width="{WIDTH}" height="0" fill="#ffffff">
        <animate attributeName="height" from="0" to="{HEIGHT}" dur="2.0s" begin="0.15s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </mask>

    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }}
      .ascii {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Courier New", monospace; font-size: 6.3px; fill: url(#asciiGrad); letter-spacing: -0.15px; }}
      .title-font {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; fill: {text_muted}; letter-spacing: 1px; }}
      .head-name {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 21px; font-weight: 800; fill: {text_primary}; letter-spacing: 0.5px; }}
      .headline {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12.5px; font-weight: 600; fill: {accent_sky}; }}
      .prompt {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; fill: {text_muted}; }}
      .prompt-cmd {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 12px; fill: {accent_cyan}; font-weight: 600; }}
      .sec-title {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; fill: {accent_violet}; font-weight: 700; letter-spacing: 1px; }}
      .key {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11.5px; fill: {accent_cyan}; font-weight: 700; letter-spacing: 0.5px; }}
      .val {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11.5px; fill: {text_secondary}; font-weight: 500; }}
      .val-bold {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11.5px; fill: {text_primary}; font-weight: 700; }}
      .tag {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 10px; fill: {badge_text}; font-weight: 700; letter-spacing: 0.5px; }}
      .dot {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11.5px; fill: {text_faint}; font-weight: 400; }}
      .faint {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; font-size: 11px; fill: {text_faint}; }}
      .accent-green {{ fill: {accent_emerald}; font-weight: 700; }}
      .cursor {{ fill: {accent_cyan}; font-weight: 900; }}
      text, tspan {{ white-space: pre; }}
    </style>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="{WIDTH}" height="{HEIGHT}" rx="20" fill="url(#bgGrad)"/>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="20" fill="url(#scanlines)"/>

  <!-- Outer Luminous Border -->
  <rect x="2" y="2" width="{WIDTH - 4}" height="{HEIGHT - 4}" rx="19" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" opacity="0.75">
    <animate attributeName="opacity" values="0.55;0.95;0.55" dur="4s" repeatCount="indefinite"/>
  </rect>

  <!-- Top Terminal Chrome Titlebar -->
  <g id="titlebar">
    <rect x="20" y="16" width="1140" height="36" rx="10" fill="{titlebar_bg}" fill-opacity="{titlebar_opacity}" stroke="{titlebar_border}" stroke-width="1"/>
    
    <!-- Window Action Dots -->
    <circle cx="40" cy="34" r="5" fill="#EF4444">
      <animate attributeName="opacity" values="1;0.6;1" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="58" cy="34" r="5" fill="#F59E0B">
      <animate attributeName="opacity" values="1;0.6;1" dur="3.5s" begin="0.3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="76" cy="34" r="5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.6;1" dur="3.5s" begin="0.6s" repeatCount="indefinite"/>
    </circle>

    <!-- Center Session Title -->
    <text x="590" y="38" text-anchor="middle" class="mono title-font">boopalan@devos: ~/workspace/profile (zsh) — 60fps</text>

    <!-- Right Live Telemetry Status -->
    <circle cx="1108" cy="34" r="4.5" fill="{accent_emerald}">
      <animate attributeName="opacity" values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/>
      <animate attributeName="r" values="4;5.5;4" dur="1.4s" repeatCount="indefinite"/>
    </circle>
    <text x="1120" y="38" class="mono tag" fill="{accent_emerald}">ONLINE</text>
  </g>

  <!-- ==================== LEFT COLUMN: VISUAL / IDENTITY ==================== -->
  <g id="left-column">
    <!-- Main Left Card Surface -->
    <rect x="20" y="64" width="446" height="526" rx="14" fill="{card_bg}" fill-opacity="{card_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="0.45"/>

    <!-- Left Card Header -->
    <g transform="translate(36, 88)">
      <circle cx="4" cy="-4" r="3" fill="{accent_cyan}"/>
      <text x="14" y="0" class="mono title-font" fill="{accent_cyan}" font-weight="700">VISUAL.MAP // NEURAL MATRIX 01</text>
      <text x="414" y="0" text-anchor="end" class="mono faint">ASCII 53x92</text>
    </g>

    <!-- ASCII Portrait Render with SMIL Staggered Reveal Mask -->
    <g mask="url(#portraitReveal)">
      <text class="ascii">
        {"\n".join(ascii_tspans)}
      </text>
    </g>

    <!-- Laser Scanning Line (Clean line, no muddy smudge) -->
    <g clip-path="url(#leftCardClip)">
      <line x1="20" y1="64" x2="466" y2="64" stroke="url(#laserGrad)" stroke-width="2">
        <animateTransform attributeName="transform" type="translate" from="0 0" to="0 520" dur="5s" repeatCount="indefinite"/>
      </line>
    </g>

    <!-- Identity Sub-Card: Architectural Philosophy (100% Unique, Zero Repetition) -->
    <rect x="34" y="492" width="418" height="84" rx="10" fill="{subcard_bg}" fill-opacity="{subcard_bg_opacity}" stroke="{badge_border}" stroke-width="1"/>
    
    <g transform="translate(48, 511)">
      <text class="mono prompt">~/matrix $ <tspan class="prompt-cmd">cat manifest.json</tspan></text>
      <text y="18" class="mono val"><tspan class="key">&gt; SPECIALTY :</tspan> Distributed APIs &amp; Vision Workflows</text>
      <text y="36" class="mono val"><tspan class="key">&gt; APPROACH  :</tspan> Turning complex data into intuitive software</text>
      <text y="54" class="mono val"><tspan class="key">&gt; MOTTO     :</tspan> <tspan class="val-bold">&quot;Resilient systems, clean code, zero bloat.&quot;</tspan></text>
    </g>
  </g>

  <!-- ==================== RIGHT COLUMN: SYSTEM.INFO ==================== -->
  <g id="right-column">
    <!-- Main Right Card Surface -->
    <rect x="484" y="64" width="676" height="526" rx="14" fill="{card_bg}" fill-opacity="{card_bg_opacity}" stroke="url(#borderGrad)" stroke-width="1" opacity="0.45"/>

    <!-- Right Header Telemetry -->
    <g transform="translate(504, 88)">
      <circle cx="4" cy="-4" r="3" fill="{accent_cyan}"/>
      <text x="14" y="0" class="mono title-font" fill="{accent_cyan}" font-weight="700">SYSTEM.INFO // TELEMETRY &amp; ARCHITECTURE</text>
      <text x="636" y="0" text-anchor="end" class="mono faint">NODE: BENGALURU-IN // PROD</text>
      <line x1="0" y1="12" x2="636" y2="12" stroke="{divider_stroke}" stroke-width="1"/>
    </g>

    <!-- Terminal Command Execution -->
    <g transform="translate(504, 120)">
      <text class="mono prompt">boopalan@devos:~$ <tspan class="prompt-cmd">./profile.sh --status --inspect</tspan></text>
    </g>

    <!-- Hero Identity & Badges with Role Rotation -->
    <g transform="translate(504, 150)">
      <text class="mono head-name">BOOPALAN S</text>
      
      <!-- Role Badge Pill Container -->
      <rect x="160" y="-18" width="186" height="24" rx="4" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1"/>
      
      <!-- Rotating Role Labels via SMIL -->
      <g>
        <text x="253" y="-2" text-anchor="middle" class="mono tag" fill="{accent_sky}">
          FULL STACK ENGINEER
          <animate attributeName="opacity" values="1;1;0;0;0;0;1" keyTimes="0;0.30;0.34;0.64;0.68;0.96;1" dur="9s" repeatCount="indefinite"/>
        </text>
        <text x="253" y="-2" text-anchor="middle" class="mono tag" fill="{accent_emerald}" opacity="0">
          BACKEND &amp; GO DEV
          <animate attributeName="opacity" values="0;0;1;1;0;0;0" keyTimes="0;0.32;0.36;0.64;0.68;0.98;1" dur="9s" repeatCount="indefinite"/>
        </text>
        <text x="253" y="-2" text-anchor="middle" class="mono tag" fill="{accent_violet}" opacity="0">
          AI WORKFLOWS DEV
          <animate attributeName="opacity" values="0;0;0;0;1;1;0" keyTimes="0;0.64;0.68;0.96;0.98;1;1" dur="9s" repeatCount="indefinite"/>
        </text>
      </g>

      <!-- Exp Pill -->
      <rect x="356" y="-18" width="102" height="24" rx="4" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1"/>
      <circle cx="370" cy="-6" r="3.5" fill="{accent_emerald}"/>
      <text x="410" y="-2" text-anchor="middle" class="mono tag" fill="{accent_emerald}">2+ YRS EXP</text>

      <!-- Mission Statement (No repeated tech keywords) -->
      <text y="22" class="mono headline">Architecting High-Throughput Microservices &amp; Intelligent Workflows</text>
    </g>

    <!-- Section 1: Core System Telemetry (Distinct, Non-Overlapping Information) -->
    <g transform="translate(504, 204)">
      <!-- Row 1: Location & Status -->
      <text y="0" class="mono"><tspan class="key">&gt; LOCATION    :</tspan> <tspan class="val-bold">Bangalore, Karnataka, India</tspan>  <tspan class="faint">[</tspan><tspan class="tag" fill="{accent_emerald}">● BENGALURU, IN</tspan><tspan class="faint">]</tspan></text>

      <!-- Row 2: Education -->
      <text y="20" class="mono"><tspan class="key">&gt; EDUCATION   :</tspan> <tspan class="val">MCA (Master of Computer Applications) · Bharathiar Univ</tspan></text>

      <!-- Row 3: Domain Focus -->
      <text y="40" class="mono"><tspan class="key">&gt; DOMAIN      :</tspan> <tspan class="val">Document Graph Parsing, Queue Orchestration &amp; Web Apps</tspan></text>

      <!-- Row 4: Production Workflow -->
      <text y="60" class="mono"><tspan class="key">&gt; WORKFLOW    :</tspan> <tspan class="accent-green">✓</tspan> <tspan class="val">Designing</tspan>  <tspan class="dot">•</tspan>  <tspan class="accent-green">✓</tspan> <tspan class="val">Scaling</tspan>  <tspan class="dot">•</tspan>  <tspan class="accent-green">✓</tspan> <tspan class="val">Shipping Production Code</tspan></text>
    </g>

    <!-- Section 2: Technical Architecture & Stack (The Sole Source of Truth for Tech) -->
    <g transform="translate(504, 300)">
      <text y="0" class="mono sec-title">[ TECHNICAL ARCHITECTURE &amp; STACK ]</text>
      
      <text y="20" class="mono"><tspan class="key">&gt; LANGUAGES   :</tspan> <tspan class="val-bold">TypeScript</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">JavaScript</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">Go (Golang)</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">Python</tspan> <tspan class="dot">·</tspan> <tspan class="val">SQL</tspan></text>

      <text y="40" class="mono"><tspan class="key">&gt; FRONTEND    :</tspan> <tspan class="val-bold">React.js</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">Next.js (App Router)</tspan> <tspan class="dot">·</tspan> <tspan class="val">Tailwind CSS</tspan> <tspan class="dot">·</tspan> <tspan class="val">HTML5</tspan></text>

      <text y="60" class="mono"><tspan class="key">&gt; BACKEND/API :</tspan> <tspan class="val-bold">Go HTTP / Chi</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">Node.js</tspan> <tspan class="dot">·</tspan> <tspan class="val">Express</tspan> <tspan class="dot">·</tspan> <tspan class="val">REST APIs</tspan> <tspan class="dot">·</tspan> <tspan class="val">WebSockets</tspan></text>

      <text y="80" class="mono"><tspan class="key">&gt; DATA &amp; AI   :</tspan> <tspan class="val-bold">PostgreSQL</tspan> <tspan class="dot">·</tspan> <tspan class="val">MongoDB</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">BullMQ</tspan> <tspan class="dot">·</tspan> <tspan class="val-bold">GLM-OCR / Vision AI</tspan> <tspan class="dot">·</tspan> <tspan class="val">AWS S3</tspan></text>

      <text y="100" class="mono"><tspan class="key">&gt; INFRA/DEVOPS:</tspan> <tspan class="val">Docker</tspan> <tspan class="dot">·</tspan> <tspan class="val">Linux System</tspan> <tspan class="dot">·</tspan> <tspan class="val">Git &amp; GitHub Actions</tspan> <tspan class="dot">·</tspan> <tspan class="val">Postman CI</tspan></text>
    </g>

    <!-- Section 3: Verified Projects (Proof of Engineering) -->
    <g transform="translate(504, 436)">
      <text y="0" class="mono sec-title">[ VERIFIED BUILDS &amp; SYSTEMS ]</text>
      
      <text y="20" class="mono"><tspan class="key">&gt; DevBench    :</tspan> <tspan class="val-bold">Developer syntax &amp; diff workbench</tspan>  <tspan class="faint">[</tspan><tspan class="tag" fill="{accent_sky}">devbenchio.vercel.app</tspan><tspan class="faint">]</tspan></text>

      <text y="40" class="mono"><tspan class="key">&gt; WindBoard   :</tspan> <tspan class="val-bold">Real-time collaborative canvas</tspan>     <tspan class="faint">[</tspan><tspan class="tag" fill="{accent_sky}">wind-board.vercel.app</tspan><tspan class="faint">]</tspan></text>
    </g>

    <!-- Section 4: Live Links & Interactive Terminal Prompt (Seamless Cursor) -->
    <g transform="translate(504, 514)">
      <!-- Links Row -->
      <text y="0" class="mono"><tspan class="key">&gt; CONNECT     :</tspan> <tspan class="val">boopalan-d3v.vercel.app</tspan> <tspan class="dot">·</tspan> <tspan class="val">github: Boopalan-d3v</tspan> <tspan class="dot">·</tspan> <tspan class="val">in: boopalans01</tspan></text>

      <!-- Bottom Terminal Prompt Line with Seamless Cursor -->
      <g transform="translate(0, 24)">
        <text class="mono prompt">boopalan@devos:~$ <tspan class="prompt-cmd">echo $CONTACT</tspan> <tspan class="faint">--&gt;</tspan> <tspan class="val-bold">boopalans0112@gmail.com</tspan><tspan class="cursor"> █<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite"/></tspan></text>
      </g>
    </g>
  </g>
</svg>"""

    output_file = f"{theme}.svg"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated {output_file} successfully ({len(svg_content)} bytes).")

generate_svg("dark")
generate_svg("light")
