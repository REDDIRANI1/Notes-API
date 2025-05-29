from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework import filters

class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.note_set.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        # Only return notes for the logged-in user
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user field when creating a note
        serializer.save(user=self.request.user)
