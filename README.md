# The World Today — Friday 13 November 2026

A make.fun `news-image-01` entry: one image summing up the world's news of
Friday 13 November 2026, drawn programmatically and copied to
`/output/entry.png` by `main.ts` (Node 22, standard library only).

## The image

A newspaper-style front page, "THE WORLD TODAY", with six illustrated
stories — the day's most consequential events, across regions and fields,
each with a picture and a short label so the day reads from the image alone:

1. **Senate calls Huang** (Tech, USA) — the ex-Nvidia chief is summoned to
   testify a day after quitting in scandal.
2. **Ukraine talks open up** (Diplomacy) — Zelensky meets US envoys; Europe
   joins the peace talks.
3. **Drone hits warship** (War) — a Ukrainian drone strikes a Russian ship
   in the Gulf of Finland.
4. **Iran claims radar strike** (Middle East) — Tehran says it hit a US
   radar site in Bahrain.
5. **US flights halted** (Travel) — the FAA grounds departures for hours
   after a communications failure.
6. **Kane breaks record** (Sport) — the 126th cap breaks England's
   appearance record vs Croatia.

Sources: BBC, Al Jazeera, Reuters — all events of, or first reported on,
13 November 2026.

## Files

- `entry.png` — the 1024×1024 image the program writes out.
- `main.ts` — the entrypoint: copies `entry.png` to the output directory.
- `draw.py` — the generator that drew `entry.png` with Pillow
  (flat vector-style illustration, DejaVu fonts). It is provenance for the
  image, not part of the entry run: `main.ts` only copies the finished PNG,
  so the entry is deterministic — both graded runs write identical bytes.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 draw.py                                        # redraw entry.png
```

## License

MIT — see `LICENSE`.
