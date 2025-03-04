# Changelog

All notable changes to this project will be documented in this file.

## [v0.2.1] - 2025-03-04

### Added

- Support for nesting lists
- Support for links in documents
- New examples added

### Changed

- Examples refactored

### Fixed

- Fixed formatting of sources
- Fixed handling of newlines in Paragraphs

## [v0.2.0] - 2025-02-25

### Added

- Added support for embedding Paragraphs into lists
- Added example of text wrapping with lists
- Added support for code blocks

### Changed

- Examples broken up into multiple scripts
- Updated pyproject.toml to support newer versions of pdm and drop support of
  pdm <= v19
- Reworked lists implementation to share code between both types (ordered and
  unordered)

### Fixed

- Fixed filename suffixes (missing .md suffix)
- Fixed the erroneous logger defaults being set by package
- Fixed the indentation of multiline list items

## [v0.1.0] - 2025-02-11

- Initial release with support for text content and lists of text.
