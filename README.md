# Digital Research Sustainability

This is a lesson implemented using [The Carpentries Workbench].

[The Carpentries Workbench]: https://github.com/carpentries/workbench-docker

## Development

A dockerised setup is provided for lesson development.

Run `docker compose up` to start the development server. After a few moments the site
will be accessible at <http://127.0.0.1:4321>. As you save changes to files in the
repository the development server will automatically detect these and rebuild the site
content. You will need to refresh your browser to see the updated content.

### Content

sntoaheusntoaheusntoaues

The [The Carpentries Workbench] uses Pandoc-flavoured markdown. This is covered in
detail in [Introduction to The Carpentries Workbench: Episode 2].

[Introduction to The Carpentries Workbench: Episode 2]: https://carpentries.github.io/sandpaper-docs/episodes.html

### Linting

A pre-commit hook for [markdownlint-cli] is used to enforce consistent style and formatting.

There is one known issue as markdownlint does not support the [link_attributes] markdown
extension. This primarily comes up when specifying the alt text for images. It manifests
as markdownlint erroneously applying a line length check when it should not. In this
case the error has to be explicitly ignored, e.g.:

```markdown
<!-- markdownlint-disable-next-line line-length -->
![You belong in The Carpentries!](https://raw.githubusercontent.com/carpentries/logo/master/Badge_Carpentries.svg){alt='Blue Carpentries hex person logo with no text.'}
```

[markdownlint-cli]: https://github.com/igorshubovych/markdownlint-cli
[link_attributes]: https://pandoc.org/MANUAL.html#extension-link_attributes
