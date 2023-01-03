#https://topaz.github.io/paste/#XQAAAQCTCQAAAAAAAAAzHIoib6kyWINtQKRrTdUO4wQMV8tuN7IVYpPXf2NB0UeuMUt2oDSKRGJY8vgiuSGFZXUqp7M7WKZTgA9On5bdlRMeftNHGaQTPge5zKjq077w4ab01Nkxyk2nogV/Z4AaHXPC8wG8Ebahi76f+btXZq7thb50WbptmZb4mW2xBCmnH4KdgBCsgbTh+fgNqQIr9YMKbMkJyp/VxbTyo97CNp3jrgX4Q2Mdw7+VUIkvO/nL/nokDJ+Vl0gpNmK8NoNpkif8WdhAfk0s//cwQuaFCGjkUWdMUrW10GF9J8O528I/tA/DYsJ7MXFZTeNTWPC5j2NksCL09+jz98qBORs5OfFRInrdzM1JTL+uWv7fmg1qVqJ0hC18yLudHih/G7LqrRmzU4zufDv9kDLyKPY7+pEF8tTOvQJE0I2TFHhBVil3vj+2vxLD/V0/Yx2F3T+JVsyQuspq4/+4psgjE8gm9w6D9ObSWT3uBCZeD2gO+LKacArg2lgGcbCLfuvbLk1XyLTRv2CeFJO7QOAJPQe1oo+efo1fjs4kuJMRtI9AJQVvB92DSDyYBJJhyI0eYT1ybTvEvkbfxrsz6yIYwDuDNslMBmtxFn3VMBMwSbsEmDK4OPBaCh+CBuaq4T2V3aM0P9klkphErtHH2e5orhcS2VnNzGcpcykSV1NHT0dN71eHbd7yhqmb31GNJFCSXqgH5ZnnGD3X6dQGmLyzT/lTjTFGT8hCM6+Jj8fxebc6XvRUTR1hO+3yyMnp5qlxxlMr9g6gLreol9M7s4U9cr4UYEVqOafJE+81yuGGAv0sgFKIxjMktAuq+kSDz76hPGRQL3RaTsN9qmm+MzkVsJhYEDvN7dGbxIm4FfmbKwfy9UOwFLDg529slz7FEVjUKH52leGohniTLDicymLKQ8KkbocllzJ7nvky/zQebUIe+U+eNHGj39G5LBXwUefhwVFt8Yo8oIdjRv45xZgMXaI2BnToVBn2rWchUKSIqihZrgLsGqUnjml/HRAhlCswjoOmgNRzJOZab6BtLnTvps17x2w4gEwV8+5Ks8fxhShGBmOgmcWOyMr7FC/g6StbHO1uC5t3u2pJ/GAR9/Cqy2ue5AUgFVrevr3aw5Wx5bwv46krTzo/WYSoRpMWASEpBxvd0bnKnpWfCL3BfOrFPz7fy6Q5AZog06eexFms1k/bG3Uf4G6Tqj5emetrVV1bycs6TP+nboX5
from .util import getinput
from itertools import cycle

s = getinput(17).strip()

rocks = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##
"""

rocks = [
    [
            (i, j)
                    for j, l in enumerate(reversed(g.splitlines()))
                                for i, c in enumerate(l)
                                            if c == "#"
                                                    ]
                                                        for g in rocks.split("\n\n")
                                                            ]

                                                            RIGHT = 5
                                                            LEFT = -3
                                                            FLOOR = 0
                                                            tip = 0
                                                            placed = set()


                                                            class Recorder:
                                                                def __init__(self) -> None:
                                                                        self.enabled = False
                                                                                self.logs = []

                                                                                    def start(self, tip, placed, ir, ig):
                                                                                            self.enabled = True
                                                                                                    self.tip = tip
                                                                                                            self.placed = {*placed}
                                                                                                                    self.ir = ir
                                                                                                                            self.ig = ig

                                                                                                                                def add_record(self, bumped, rock):
                                                                                                                                        if self.enabled and (not bumped or will_bump(rock, self.placed)):
                                                                                                                                                        self.logs.append((bumped, rock))

                                                                                                                                                            def can_replay(self, tip, placed, ir, ig):
                                                                                                                                                                    return (
                                                                                                                                                                                self.logs
                                                                                                                                                                                            and (self.ir - ir) % len(rocks) == 0
                                                                                                                                                                                                        and (self.ig - ig) % len(s) == 0
                                                                                                                                                                                                                    and all(
                                                                                                                                                                                                                                    bumped
                                                                                                                                                                                                                                                    == will_bump(((x, y + tip - self.tip) for x, y in blocks), placed)
                                                                                                                                                                                                                                                                    for bumped, blocks in self.logs
                                                                                                                                                                                                                                                                                    )
                                                                                                                                                                                                                            )


                                                                                                                                                                    def will_bump(rock, placed):
                                                                                                                                                                        return any(
                                                                                                                                                                                x == RIGHT or x == LEFT or y == FLOOR or (x, y) in placed for x, y in rock
                                                                                                                                                                                    )


                                                                                                                                                                        offset = 0
                                                                                                                                                                        target = 1000000000000
                                                                                                                                                                        GUESS = 3000  # must be in a cycle after this many rocks
                                                                                                                                                                        recorder = Recorder()
                                                                                                                                                                        ig = 0
                                                                                                                                                                        for ir, rock in enumerate(cycle(rocks)):
                                                                                                                                                                                if recorder.can_replay(tip, placed, ir, ig):
                                                                                                                                                                                            P = ir - recorder.ir
                                                                                                                                                                                                    skipped = (target - ir) // P
                                                                                                                                                                                                            target -= skipped * P
                                                                                                                                                                                                                    offset += skipped * (tip - recorder.tip)
                                                                                                                                                                                                                        if ir >= GUESS and ir % len(rr) == target % len(rr):
                                                                                                                                                                                                                                    if not recorder.enabled:
                                                                                                                                                                                                                                                    recorder.start(tip, placed, ir, ig)
                                                                                                                                                                                                                                                        if ir == 2022:
                                                                                                                                                                                                                                                                    print(tip)
                                                                                                                                                                                                                                                                        if ir == target:
                                                                                                                                                                                                                                                                                    print(tip + offset)
                                                                                                                                                                                                                                                                                            break
                                                                                                                                                                                                                                                                                                r = [(x, y + tip + 4) for x, y in rock]
                                                                                                                                                                                                                                                                                                    while True:
                                                                                                                                                                                                                                                                                                                dx = -1 if s[ig % len(s)] == "<" else 1
                                                                                                                                                                                                                                                                                                                        ig += 1
                                                                                                                                                                                                                                                                                                                                rr = [(x + dx, y) for x, y in r]
                                                                                                                                                                                                                                                                                                                                        if not (bumped := will_bump(rr, placed)):
                                                                                                                                                                                                                                                                                                                                                        r = rr
                                                                                                                                                                                                                                                                                                                                                                recorder.add_record(bumped, rr)
                                                                                                                                                                                                                                                                                                                                                                        rr = [(x, y - 1) for x, y in r]
                                                                                                                                                                                                                                                                                                                                                                                bumped = will_bump(rr, placed)
                                                                                                                                                                                                                                                                                                                                                                                        recorder.add_record(bumped, rr)
                                                                                                                                                                                                                                                                                                                                                                                                if not bumped:
                                                                                                                                                                                                                                                                                                                                                                                                                r = rr
                                                                                                                                                                                                                                                                                                                                                                                                                        else:
                                                                                                                                                                                                                                                                                                                                                                                                                                        break
                                                                                                                                                                                                                                                                                                                                                                                                                                            tip = max(tip, max(y for x, y in r))
                                                                                                                                                                                                                                                                                                                                                                                                                                                placed.update(r)

