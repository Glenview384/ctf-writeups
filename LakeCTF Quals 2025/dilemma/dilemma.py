import socket
import re
import time

HOST = "chall.polygl0ts.ch"
PORT = 6667

def recv_until(sock, marker, timeout=10):
    data = ""
    start_time = time.time()
    while marker not in data:
        if time.time() - start_time > timeout:
            print("[!] Timeout waiting for marker")
            break
        try:
            sock.settimeout(0.1)
            part = sock.recv(4096).decode(errors="ignore")
            if not part:
                break
            data += part
            print(part, end="")
        except socket.timeout:
            continue
        except Exception as e:
            print(f"[!] Error receiving: {e}")
            break
    return data

def extract_boxes(text):
    boxes = {}
    for match in re.finditer(r"[Tt]he box (\d+) contains number (\d+)", text):
        box_num = int(match.group(1))
        number = int(match.group(2))
        boxes[box_num] = number
    return boxes

def get_current_player(text):
    matches = list(re.finditer(r"Provide Python script for player (\d+)", text))
    if matches:
        return int(matches[-1].group(1))
    
    matches = list(re.finditer(r"You are player number (\d+)", text))
    if matches:
        return int(matches[-1].group(1))
    
    return None

def main():
    s = socket.socket()
    s.connect((HOST, PORT))
    print("[+] Connected")
    
    full_history = ""
    processed_players = set() 
    
    while True:
        data = recv_until(s, "Provide Python script for player", timeout=15)
        
        if not data:
            print("[!] No data received, reconnecting...")
            break
        
        full_history += data
        
        if "Welcome to the 100 Prisoners Problem" in data:
            print("\n[*] New game started")
            processed_players.clear()
            full_history = data
        
        player = get_current_player(full_history)
        
        if not player:
            print("[!] Cannot identify player")
            continue
        
        if player in processed_players:
            print(f"[*] Player {player} is already successded, skipping...")
            continue
        
        print(f"\n[PLAYER {player}] Starting...")
        
        boxes = extract_boxes(full_history)
        print(f"[PLAYER {player}] Known boxes: {len(boxes)}")
        
        target_number = player
        box_with_target = None
        
        for box_num, number_inside in boxes.items():
            if number_inside == target_number:
                box_with_target = box_num
                break
        
        if box_with_target:
            script = f"print({box_with_target})"
            print(f"[PLAYER {player}] ✓ Found box {box_with_target} with number {target_number}")
        else:
            known_boxes = set(boxes.keys())
            start = 1
            
            while start in known_boxes and start <= 100:
                start += 1
            
            script = f"for i in range({start}, 101):\n    print(i)"
            print(f"[PLAYER {player}] Searching from box {start}")
        
        try:
            s.sendall((script.rstrip() + "\nEOF\n").encode())
            print(f"[PLAYER {player}] Sent a script")
            processed_players.add(player)
        except Exception as e:
            print(f"[!] Error: {e}")
            break
        
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Stopped by user")
    except Exception as e:
        print(f"\n[!] Error: {e}")
