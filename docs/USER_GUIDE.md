# Editor workflow

This is a promo selection and review tool. It returns source cut lists and text previews; it does not render videos.

1. Start the app with `python -m streamlit run app.py`.
2. Open **Prepare & run**. Choose a folder, upload timestamped episode `.txt` files, or paste one timestamped episode script.
3. Check the parsed episode count. Every file needs an episode number, scene headings and scene start/end times, plus timestamped camera, action and dialogue blocks. See `examples/episode-001.txt` for the accepted format. Untimed prose cannot provide exact footage cut points.
4. Select episodes, model names and maximum candidates. Use a fresh output folder for changed inputs/settings. Click **Select and judge selected episodes**. This uses your configured OpenAI API account.
5. Choose the resulting saved run in the sidebar. Saved results do not trigger API calls.
6. In **Episode review**, compare the proposed cuts. **First 3 seconds** exposes the opening evidence; **Assembled promo** shows each segment in playback order; **Source references** traces original events and line numbers.
7. Leave model scores hidden for a first impression, then inspect the evidence and score breakdown. Mark approve/reject/needs-review and add notes. Human decisions do not silently rewrite model scores or remove timing uncertainty.
8. In **Compare & export**, enable model scores to see posting priority. Download all comparisons or the qualifying global order. Expand coverage to see episodes with weak, absent or failed selections.

Each candidate uses one episode. A joined candidate can select up to three chronological, non-overlapping intervals from that episode. Cross-episode series promos are outside the current scope.

The global list is ordered by weighted editorial score. Score ties remain ties; suggested posting order breaks ties by cliffhanger strength, newcomer clarity, opening impact and then a stable identifier. Episode number receives no preference. A separate one-per-episode queue uses the best qualifying selection from each episode; unqualified best-effort cuts remain in the episode report.

Use the exported timestamps in your video editor to assemble the actual footage. Check exact word timing, visual delivery, transitions and the final frame before posting. These script-based scores are editorial suggestions, not measured predictions of views or conversions.

To review the confidential full-pack outputs without API access, extract the separate raw-output archive into this project so `runs/full/inventory.json` exists. The archive is for the assignment's intended recipients. The source package's cached `runs/demo` is synthetic and can be shared independently.
