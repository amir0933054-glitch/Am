from datetime import datetime

class MemberManagement:
    def __init__(self):
        self.members = {}

    def add_member(self, member_id, member_info):
        """Add a new member."""
        if member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member_id] = member_info

    def remove_member(self, member_id):
        """Remove a member by ID."""
        if member_id not in self.members:
            raise ValueError("Member ID does not exist.")
        del self.members[member_id]

    def update_member(self, member_id, member_info):
        """Update member information."""
        if member_id not in self.members:
            raise ValueError("Member ID does not exist.")
        self.members[member_id] = member_info

    def get_member(self, member_id):
        """Get member information by ID."""
        return self.members.get(member_id, None)

    def list_members(self):
        """List all members."""
        return self.members

    def current_time(self):
        """Return current date and time in UTC."""
        return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

# Example Usage
if __name__ == "__main__":
    manager = MemberManagement()
    print("Current Date and Time (UTC):", manager.current_time())