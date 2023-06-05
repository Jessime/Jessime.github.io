# My site

## Setup

Roughly following [this post](https://www.earthinversion.com/blogging/how-to-install-jekyll-on-appple-m1-macbook/) with a few tweaks.


```
brew install rbenv ruby-build;
rbenv install 3.0.0;rbenv global 3.0.0;ruby -v;rbenv rehash
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
gem install --user-install bundler jekyll
echo 'export PATH="/usr/local/opt/ruby/bin:/usr/local/lib/ruby/gems/3.0.0/bin:$PATH"' >> ~/.zshrc
cd ~/Code/me/Jessime.github.io/
mkdir /Users/jessime/Data/bundle
bundle config path /Users/jessime/Data/bundle
bundle update
# bundle add webrick  # Probably not needed anymore
# bundle install --redownload  # Probably not needed anymore
```

### And run

```
bundle exec jekyll serve
```

## Minimal Mistakes remote theme starter

Fork this repo for the quickest method of getting started with the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes).

Contains basic configuration to get you a site with:

- Sample posts.
- Sample top navigation.
- Sample author sidebar with social links.
- Sample footer links.
- Paginated home page.
- Archive pages for posts grouped by year, category, and tag.
- Sample about page.
- Sample 404 page.
- Site wide search.

Replace sample content with your own and [configure as necessary](https://mmistakes.github.io/minimal-mistakes/docs/configuration/).

---

### Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.
