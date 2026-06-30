"""Subprocess runner for webapp bridge. Called by uzi_bridge.py via subprocess."""
import sys
import os
import traceback

if __name__ == "__main__":
    try:
        ticker = sys.argv[1]
    except IndexError:
        print("ERR: missing ticker argument", file=sys.stderr)
        sys.exit(1)

    try:
        from lib.pipeline.run import run_pipeline
        report_path = run_pipeline(ticker, resume=True)
        print(report_path, flush=True)
    except Exception:
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
