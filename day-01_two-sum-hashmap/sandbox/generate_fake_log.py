#!/usr/bin/env python3
import argparse, random, datetime, pathlib

TEMPLATES_INFO = [
    "INFO - Service started",
    "INFO - Health check OK",
    "INFO - Request completed in {ms}ms",
    "DEBUG - Cache hit for key={key}",
    "DEBUG - Retrying operation",
]

TEMPLATES_WARN = [
    "WARN - Slow response {ms}ms",
    "WARN - Disk usage at {pct}%",
    "WARN - High memory usage {pct}%",
]

TEMPLATES_ERROR = [
    "ERROR - Connection failed",
    "ERROR - Timeout while calling dependency",
    "ERROR - Permission denied",
    "ERROR - Unexpected exception in handler",
]

def line(template):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ms = random.randint(5, 900)
    pct = random.randint(70, 99)
    key = random.choice(["user:123", "cfg:env", "srv:auth", "pod:api-1"])
    return f"{now} {template.format(ms=ms, pct=pct, key=key)}"

def main():
    parser = argparse.ArgumentParser(description="Generate a fake mixed log file.")
    parser.add_argument("--errors", type=int, default=10, help="Approx number of ERROR lines")
    parser.add_argument("--length", type=int, default=200, help="Total lines in log")
    parser.add_argument("--out", default="system.log", help="Output log filename")
    args = parser.parse_args()

    path = pathlib.Path(args.out)
    lines = []

    # guarantee some ERROR lines
    for _ in range(args.errors):
        lines.append(line(random.choice(TEMPLATES_ERROR)))

    # fill remaining with INFO/WARN/DEBUG
    remaining = max(0, args.length - len(lines))
    pools = [TEMPLATES_INFO, TEMPLATES_WARN, TEMPLATES_INFO, TEMPLATES_INFO, TEMPLATES_WARN]
    for _ in range(remaining):
        tmpl_pool = random.choice(pools)
        lines.append(line(random.choice(tmpl_pool)))

    random.shuffle(lines)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} lines to {path}")

if __name__ == "__main__":
    main()

