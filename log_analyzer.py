def analyze_logs(logs):
    total_attempts = len(logs)
    failed_attempts = 0
    failure_counts = {}
    for username, success in logs:
        if success is False:
            failed_attempts += 1
            if username not in failure_counts:
                failure_counts[username] = 1
            else:
                failure_counts[username] += 1
    repeat_offenders = []
    for username, count in failure_counts.items():
        if count > 1:
            repeat_offenders.append(username)
    return {
        "total": total_attempts,
        "failed_attempts": failed_attempts,
        "repeat_offenders": repeat_offenders
    }
