from django.http import JsonResponse
from django.db.models import Q
from api.models import Department, Position

def homework_querysets(request):
    # 1. Departments with manager positions, ordered by name
    departments_with_managers = Department.objects.filter(
        position__is_manager=True
    ).order_by("name").distinct()

    # 2. Count of active positions
    active_positions_count = Position.objects.filter(is_active=True).count()

    # 3. Positions that are active OR belong to HR department
    active_or_hr_positions = Position.objects.filter(
        Q(is_active=True) | Q(department__name="HR")
    )

    # 4. Department names with managers
    department_names_with_managers = Department.objects.filter(
        position__is_manager=True
    ).values("name").distinct()

    # 5. All positions, ordered by title, only title and is_active
    sorted_positions = Position.objects.order_by("title").values("title", "is_active")

    return JsonResponse({
        "departments_with_managers": list(departments_with_managers.values("name")),
        "active_positions_count": active_positions_count,
        "active_or_hr_positions": list(active_or_hr_positions.values("title", "is_active")),
        "department_names_with_managers": list(department_names_with_managers),
        "sorted_positions": list(sorted_positions),
    })
