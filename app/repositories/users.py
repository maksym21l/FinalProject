from app.utils.error_handler import UserNotFoundError


def get_user_by_id_or_error(session: Session, user_id: int) -> User:
    user = session.query(User).filter(user_id == User.user_id).first()
    if not user:
        raise UserNotFoundError(
            message=f"User with id: {user_id} not found",
        )
    return user