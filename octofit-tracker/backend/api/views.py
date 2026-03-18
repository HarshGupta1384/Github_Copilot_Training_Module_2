from django.http import JsonResponse


def list_items(request, key):
    """Return a simple JSON list for each endpoint key."""
    sample_data = {
        'activities': [
            {'id': 1, 'name': 'Run', 'distance_km': 5},
            {'id': 2, 'name': 'Swim', 'distance_m': 1000},
        ],
        'leaderboard': [
            {'id': 1, 'user': 'alice', 'score': 1200},
            {'id': 2, 'user': 'bob', 'score': 1100},
        ],
        'teams': [
            {'id': 1, 'name': 'Team Rocket', 'members': 5},
            {'id': 2, 'name': 'Octo Sprinters', 'members': 8},
        ],
        'users': [
            {'id': 1, 'username': 'alice', 'email': 'alice@example.com'},
            {'id': 2, 'username': 'bob', 'email': 'bob@example.com'},
        ],
        'workouts': [
            {'id': 1, 'title': 'Morning Run', 'duration_min': 35},
            {'id': 2, 'title': 'Evening Yoga', 'duration_min': 45},
        ],
    }

    data = sample_data.get(key, [])
    # Return paginated-like structure to support .results
    return JsonResponse({'results': data})
