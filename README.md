# Old exhibitions

Prior to the publication of *Bending Lines*, LMEC released digital exhibitions in a standard format on the digital collections portal at <https://collections.leventhalmap.org/exhibits>.

As part of a larger overhaul of LMEC's two websites in 2025---namely, the main site at <https://leventhalmap.org> and the digital collections portal listed above---we deprecated the page at <https://collections.leventhalmap.org/exhibits> and migrated all of the past exhibits to our main site.

This README recaps our methods for this process.

## Exporting old exhibitions

Eben English at BPL shared this `wget` script, where `:id` is a number between 1 and 24 that identifies each old digital exhibition:

```bash
wget --convert-links --ignore-tags=a --page-requisites --no-clobber --recursive https://collections.leventhalmap.org/exhibits/:id
```

Ian ran this script to download each past exhibition, which get saved as `1.html`, `2.html`, etc., along with a bunch of other assets like favicons, bundled CSS/JS and what not. 

## Formatting filenames

Two steps here:

1. First, run [`01_organize_html.py`](/processing/01_organize_html.py) to grab the name of the exhibition, turn that into a directory, rename the HTML file to `index.html`, and place that inside the named directory.
2. Second, run [`02_strip.sh`](/processing/02_strip.sh) to remove the prefix "past-exhibitions"
3. Third, we hand-deleted unnecessary assets from the `assets` directory---this included artefactual images, icons, etc. that got yanked down with `wget` but have nothing to do with the digital exhibitions.

## Migrating to LMEC servers / Astro build

As of 2025, the LMEC main site is built in Astro. As of this writing on 10/30/2025, Astro rebuilds destructively, e.g. everything in the target directory is overwritten during build.

We keep these exhibitions on the server and in order to avoid destroying them during every Astro rebuild, we write symlinks that connect the desired URL on the client side to the build path on the server side.

There are a few steps here, specific to migrating past exhibitions from the collections portal to our main site:

1. First, we run `03_move.sh` to copy assets into each exhibition directory 
2. Second, we add all the past digital exhibitions to [this manifest of "other properties,"](https://github.com/bplmaps/lmec-main-site-astro/blob/main/public/other-properties-manifest.yaml) which our symlink script loops through each time the site rebuilds
3. Finally, we hand-copy the contents of `exhibits` from this repository into our `geoservices` server at `var/www/other-properties/legacy-digital-exhibitions`.

*et voila*, it should work now
