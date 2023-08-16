#!/usr/bin/python3
"""
    class city
"""


class City(BaseModel):
    """
        args:
            state_id: string - empty string: it will be the State.id
            name: string - empty string
    """ 
    state_id = ""
    name = ""
