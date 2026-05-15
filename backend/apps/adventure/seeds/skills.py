from apps.adventure.models import AdventureItem, AdventureSkill


TAG_TO_SKILL_INDEX = {
    AdventureItem.TAG_ARMA: 0,
    AdventureItem.TAG_COMIDA: 1,
    AdventureItem.TAG_BEBIDA: 2,
    AdventureItem.TAG_REMEDIO: 3,
    AdventureItem.TAG_MONEDA: 4,
    AdventureItem.TAG_DOCUMENTO: 5,
}


def seed_chapter_skills(chapter, skill_defs):
    skills = {}
    for idx, skill_data in enumerate(skill_defs, start=1):
        skill, _ = AdventureSkill.objects.update_or_create(
            chapter=chapter,
            slug=skill_data["slug"],
            defaults={
                "name": skill_data["name"],
                "description": skill_data["description"],
                "category": skill_data["category"],
                "emoji": skill_data["emoji"],
                "base_power": skill_data["base_power"],
                "order": idx,
            },
        )
        skills[skill_data["slug"]] = skill
    return skills


def sync_chapter_item_skills(chapter, skills_by_slug, skill_defs):
    skill_slugs = [skill_data["slug"] for skill_data in skill_defs]

    for item in AdventureItem.objects.filter(chapter=chapter):
        skill_index = TAG_TO_SKILL_INDEX.get(item.item_tag)
        skill_slug = skill_slugs[skill_index] if skill_index is not None and skill_index < len(skill_slugs) else None
        next_skill = skills_by_slug.get(skill_slug) if skill_slug else None

        if item.skill_id != (next_skill.id if next_skill else None):
            item.skill = next_skill
            item.save(update_fields=["skill"])
