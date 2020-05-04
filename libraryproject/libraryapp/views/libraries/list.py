import sqlite3
from django.shortcuts import render
from libraryapp.models import Library
from ..connection import Connection


def library_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.name,
                l.address
            from libraryapp_library l
            """)

            all_libraries = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                library = Library()
                library.id = row['id']
                library.name = row['name']
                library.address = row['address']

                all_libraries.append(library)

        template = 'libraries/list.html'
        context = {
            'all_libraries': all_libraries
        }

        return render(request, template, context)