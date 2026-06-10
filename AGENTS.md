# Repository Instructions

## CV and Experience Workflow

When the user adds or replaces the CV, keep the website CV workflow stable:

- The canonical public CV path is `assets/cv/Zhengyang_Wang_CV.pdf`.
- If the user provides a CV under another filename, copy or rename it to the canonical path and remove obsolete older CV PDFs from `assets/cv/`.
- Extract the CV text with a structured PDF reader such as `pypdf`; do not manually guess from memory.
- Update `experience.md` as a concise web companion to the CV, not a full duplicate.
- Preserve these sections when possible: Education, Research Interests, Research Experience, Publication, Projects / Technical Work, Work Experience, Selected Writing.
- Keep descriptions shorter than the CV, emphasizing research fit, optimization, routing/game-theory work, and PhD-facing academic substance.
- Keep all site links pointing to `{{ '/assets/cv/Zhengyang_Wang_CV.pdf' | relative_url }}`.
- After changes, verify that the canonical CV file exists, no stale CV link remains, YAML/front matter still parses, and `git status --short` is reviewed.

## Portrait Workflow

- The canonical portrait path is `assets/images/portrait.jpg`.
- If the portrait is replaced, generate a web-sized JPEG copy without retaining camera EXIF metadata.
- Keep the homepage portrait restrained and academic; avoid decorative effects that compete with the writing and CV content.
