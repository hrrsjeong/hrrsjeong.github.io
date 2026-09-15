# English and Korean pages

English pages keep their existing URLs. Korean pages live in `_pages/ko/` and use `/ko/` URLs. Both versions render as complete static HTML and work without JavaScript.

Each Korean page sets `lang: ko` and `translation_of` to the original English URL. The shared header uses this pair for the language switch and alternate-language metadata. Links in Korean content must point to the corresponding `/ko/` page; asset, paper, email, and external URLs remain shared. The language-switch script preserves the current query string and section anchor without redirecting visitors based on their browser settings.

Korean pages inherit page-specific CSS from their English counterpart through `_includes/page_styles.liquid`. Team content and all people pages remain in English in both languages. Their page bodies use shared includes; member profiles read education, positions, and photos from the original English page through `_layouts/member.liquid`. Korean routes set `content_lang: en` for these sections, so site navigation can stay in Korean while the profile itself stays English. Common interface labels are in `_data/locales.yml`; Korean typography and the always-visible language switch are in `_sass/_language.scss`.

When updating content, edit both language versions. Preserve names, publication titles, journals, and established technical terms where translation would be unnatural. Recruitment numbers, qualifications, contact details, and research claims should agree across languages.

News entries use `content_ko` in their front matter for the Korean home page and news list. Individual Korean news pages are also in `_pages/ko/` and link to their original news URL through `translation_of`.

After a Jekyll build, run `python3 bin/check_localization.py _site`. The deployment workflow runs this check before publishing. It validates language pairs, navigation, image paths, metadata, shared styles, and selected translated content. Check the language switch and menu at desktop and mobile sizes when changing navigation or styles.
