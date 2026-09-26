from transcript import redact, section, upsert

n = "2026-09-26-175142-hello.txt"
t = " banner\n\n❯ hi me@x.com\n● path /home/bob/x\n"
s = section(n, t)
assert "banner" not in s and "me@x.com" not in s and "/home/bob" not in s
assert "## 2026-09-26 17:51 — hi [email]" in s
log = upsert("# L\n", "hello", s)
assert upsert(log, "hello", s) == log            # idempotent
assert upsert(log, "other", section("2026-09-26-180000-other.txt", t)).count("<!-- session:") == 2
print("ok")
