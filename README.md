# Max Wang personal website

This is a GitHub Pages site built with Jekyll.

## Edit content

- Home page: `index.md`
- About page: `about.md`
- Projects page: `projects.md`
- Writing index: `writing.md`
- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Site settings: `_config.yml`
- Styles: `assets/css/style.css`

## Publish

Push the repository to `https://github.com/MaxWangZY/MaxWangZY.github.io`.
GitHub Pages will build the site with Jekyll.

## Preview locally

If Ruby and Bundler are installed:

```bash
bundle init
bundle add github-pages --group "jekyll_plugins"
bundle exec jekyll serve
```

Then open `http://localhost:4000`.
