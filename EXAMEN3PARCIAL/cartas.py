#!/usr/bin/env python3
import sys

PLAYERS = {1,2,3,4}
CARDS = 32
SETS = 8

def card_set_idx(card):
    """Carta 1..32 -> conjunto 1..8"""
    return (card - 1) // 4 + 1

def cards_of_set(s):
    """Conjunto 1..8 -> lista de cartas [1..32]"""
    base = (s - 1) * 4 + 1
    return [base + i for i in range(4)]

def parse_int(tok):
    try:
        return int(tok)
    except:
        return None

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    try:
        n = int(data[0].strip())
    except:
        print("yes")
        return

    # possible_owners[c] = set of players who could have card c
    # cards are 1..32
    possible_owners = {c: set(PLAYERS) for c in range(1, CARDS+1)}
    removed = set()  # cards already removed by a cuarteto

    line_no = 0
    for i in range(1, n+1):
        if i >= len(data)+1:
            break
        line = data[i].strip()
        line_no += 1
        if not line:
            continue
        parts = line.split()
        action = parts[0].upper()

        # ---- ASK A B C
        if action == "ASK":
            if len(parts) < 4:
                print("no", line_no); return
            A = parse_int(parts[1])
            B = parse_int(parts[2])
            C = parse_int(parts[3])
            if any(x is None for x in (A,B,C)) or not (1<=A<=4 and 1<=B<=4 and 1<=C<=32):
                print("no", line_no); return

            s = card_set_idx(C)
            cards = cards_of_set(s)

            # If for every card in set, A is NOT a possible owner -> impossible (A cannot have any card of set)
            can_have_some = any(A in possible_owners[c] for c in cards if c not in removed)
            if not can_have_some:
                print("no", line_no)
                return
            # ASK doesn't change state

        # ---- GIVE B A C  (B gives card C to A)
        elif action == "GIVE":
            if len(parts) < 4:
                print("no", line_no); return
            B = parse_int(parts[1])
            A = parse_int(parts[2])
            C = parse_int(parts[3])
            if any(x is None for x in (A,B,C)) or not (1<=A<=4 and 1<=B<=4 and 1<=C<=32):
                print("no", line_no); return

            if C in removed:
                print("no", line_no); return

            # If possible_owners says B is impossible for C -> B cannot give it => cheating
            if B not in possible_owners[C]:
                print("no", line_no)
                return

            # After giving, we know A has C for sure
            possible_owners[C] = {A}

            # Also, since A now has C, remove A from possibilities of that card's duplicates? no need
            # (we don't deduce exclusivity across cards except by direct actions)

        # ---- DENY B C  or FAIL B C  (B says they don't have C)
        elif action in ("DENY", "FAIL"):
            if len(parts) < 3:
                print("no", line_no); return
            B = parse_int(parts[1])
            C = parse_int(parts[2])
            if any(x is None for x in (B,C)) or not (1<=B<=4 and 1<=C<=32):
                print("no", line_no); return

            if C in removed:
                # if card already removed, denying is fine
                continue

            # If we already know B has C -> cheating (they denied but we know they have it)
            if possible_owners[C] == {B}:
                print("no", line_no)
                return

            # Remove B from possible owners of C
            if B in possible_owners[C]:
                possible_owners[C].discard(B)
                if len(possible_owners[C]) == 0:
                    # Nobody could have it => contradiction
                    print("no", line_no)
                    return

        # ---- RETIRA A S  or SET A S
        elif action in ("RETIRA", "SET", "REMOVE"):
            if len(parts) < 3:
                print("no", line_no); return
            A = parse_int(parts[1])
            S = parse_int(parts[2])
            if any(x is None for x in (A,S)) or not (1<=A<=4 and 1<=S<=8):
                print("no", line_no); return

            cards = cards_of_set(S)
            for c in cards:
                if c in removed:
                    # already removed -> cannot remove again
                    print("no", line_no); return
                # If possible_owners for c excludes A -> contradiction
                if A not in possible_owners[c]:
                    print("no", line_no)
                    return
            # mark removed and set owners to none
            for c in cards:
                removed.add(c)
                possible_owners[c] = set()

        else:
            # try to accept alternate verbose forms (some examples used FAIL/GIVE/RETIRA)
            # If unknown action -> error
            print("no", line_no)
            return

    # if we never found contradiction
    print("yes")


if __name__ == "__main__":
    main()
