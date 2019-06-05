import argparse

import pagexml
from joblib import Parallel, delayed


def load_paths(load_path):
    """
    Load a list of paths from a textfile at load_path
    :param load_path: str, path to textfile
    :return: list, str of paths
    """

    if load_path.endswith(".xml"):
        return [load_path]
    with open(load_path) as f:
        paths = f.read().splitlines()
    return paths


def add_baseline(pxml, node):

    coords = pxml.getPoints(node)
    left_x = coords[0].x
    right_x = coords[1].x
    top_y = coords[0].y
    bottom_y = coords[2].y
    height = bottom_y - top_y
    text_equiv = pxml.getTextEquiv(node)
    # Check for chars going below the baseline
    if [char for char in 'Qgjpqy,;' if char in text_equiv]:
        # Keep size of the box, set baseline to 0.25 offset
        pxml.setBaseline(node, left_x, bottom_y - height / 4, right_x, bottom_y - height / 4)
    else:
        # Set baseline to current bottom of the box
        pxml.setBaseline(node, left_x, bottom_y, right_x, bottom_y)
        # Expand box downwards to obtain 0.25 offset
        coords[2].y = bottom_y + height / 3
        coords[3].y = bottom_y + height / 3
        pxml.setCoords(node, coords)


def process_file(gts_path, new_path, overwrite=False, remove_text=True):
    pxml = pagexml.PageXML(gts_path)
    print(gts_path)
    gt_sizes = pxml.getPagesSize()

    entity_pxml = pagexml.PageXML(new_path)

    entity_pxml.resize(gt_sizes)

    tls = pxml.select(".//_:TextLine")
    pxml.rmElems(tls)

    # copy textlines before textregions so that removing them won't kill the entities
    pxml.copyTextLinesAssignByOverlap(entity_pxml)

    for tl in pxml.select(".//_:TextLine"):
        add_baseline(pxml, tl)
        if remove_text:
            pxml.rmElems(pxml.select(".//_:Word", tl))
            pxml.rmElems(pxml.select(".//_:TextEquiv", tl))

    if overwrite:
        out_path = gts_path
    else:
        out_path = gts_path.replace("page", "page_gts")

    pxml.write(out_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--gts_files", type=str, help="List of files from the gts")
    parser.add_argument("--new_files", type=str, help="List of files with entities")
    parser.add_argument("--joblib_threads", type=int, default=1,
                        help="Number of joblib threads. If one, joblib is not used. Default: 1")
    parser.add_argument("--overwrite", action="store_true",
                        help="Directly overwrite gts files")
    parser.add_argument("--remove_text", action="store_true",
                        help="Delete words and textequivs")

    args = parser.parse_args()

    gts_paths = load_paths(args.gts_files)
    new_paths = load_paths(args.new_files)

    if args.joblib_threads > 1:
        print("Using joblib")
        Parallel(n_jobs=args.joblib_threads)(
            delayed(process_file)(gts_path, new_path, args.overwrite, args.remove_text) for (gts_path, new_path) in
            zip(gts_paths, new_paths))
    else:
        print("Not using joblib")
        for (gts_path, new_path) in zip(gts_paths, new_paths):
            process_file(gts_path, new_path, args.overwrite, args.remove_text)
