Goal:
Generate a single-file index.html Student Profile Card with a dark-mode frosted glass (dark glassmorphism) theme, set over a copyright-free Unsplash starry-night background image, including social links, skill tags, and hover animations — written for an intermediate HTML/CSS developer.

Context:
This is a front-end design exercise to build a polished, professional-looking student profile card displaying:

- A circular profile image placeholder (gradient-filled with initials fallback)
- Student name (bold Poppins heading, prominent typography)
- Stream/course badge (e.g. Computer Science · Year 2) with a cyan dot prefix and pill styling
- Short bio (2–3 sentences, light body copy via Inter)
- Skill tags (e.g. Python, UI Design, Data Analysis, React, SQL, Figma)
- Social link icons (GitHub, LinkedIn, Email) with brand-color hover reveals
- A two-column card footer showing institution/year on the left and an "Available" status indicator (green pulsing dot) on the right

The card sits over a dark starry-night background photo (Greg Rakozy, Unsplash License — free for commercial & personal use) with a dark overlay (rgba ~0.62) so the image is visible but subdued. Use dark glassmorphism — a near-opaque dark-tinted semi-transparent panel with backdrop-filter blur, a subtle top-edge shimmer border, a thin indigo-to-cyan gradient accent line at the very top of the card, and a deep box-shadow with an indigo ambient glow. Hover effects should animate the card (lift + intensified glow) and each interactive element individually.

Fonts used:
- Poppins (600, 700) — headings and avatar initials
- Inter (300, 400, 500, 600) — body copy, labels, tags

Constraints:

- Single index.html file — no external CSS or JS files
- Must open directly in any browser with no server
- Vanilla HTML & CSS only — no frameworks or libraries except Google Fonts CDN
- Background image: Unsplash Free License photo loaded via CDN URL (no download required); dark CSS gradient overlay ensures legibility even if the image fails to load
- Use CSS custom properties (--variables) for ALL colors, blur values, gradients, and radii
- Add section comments clearly labeling: CSS Custom Properties, Layout Structure, Glassmorphism Effect, Hover Animations, Typography, Skill Tags, Social Icons, and Card Footer
- Dark glassmorphism panel must use:
    backdrop-filter: blur(18px) saturate(180%) brightness(1.05)
    background: rgba(14, 18, 35, 0.52)
    border: 1px solid rgba(255, 255, 255, 0.10)
    A 2px top-edge gradient rule via card::before (indigo → cyan)
- Skill tags: pill/badge styling, indigo-tinted background, indigo border, hover lifts with neon glow
- Social icons: inline SVG only (no icon CDN); each reveals its brand color (GitHub dark, LinkedIn blue, Gmail red) on hover with a matching colored box-shadow glow
- Avatar: CSS gradient placeholder (deep indigo → navy → dark teal) with white initials; a green status dot (emerald) with glow in the bottom-right corner
- Card footer: separated by a subtle border, dark background tint, "Available" text with an animated emerald dot on the right
- Responsive: padding and font-size adjustments at max-width 480px