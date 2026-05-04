from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from notes.setializers import NoteSerializer


class NoteList(APIView):
    def post(self, request):
        note = NoteSerializer(data=request.data, context={'request': request})
        if note.is_valid():
            note.save()
            return Response(note.data, status=status.HTTP_201_CREATED)

        return Response(note.errors, status=status.HTTP_400_BAD_REQUEST)