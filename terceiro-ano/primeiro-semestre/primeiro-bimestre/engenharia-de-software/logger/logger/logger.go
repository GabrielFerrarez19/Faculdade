package logger

import (
	"fmt"
	"os"
	"sync"
	"time"
)

const (
	LevelInfo    = "INFO"
	LevelWarning = "WARNING"
	LevelError   = "ERROR"
	LevelLog     = "LOG"
)

type Logger struct {
	mu       sync.Mutex
	entries  []string
	instanceID int64 
}

var (
	instance *Logger
	once     sync.Once
	idCounter int64
)

func init() {
	idCounter = time.Now().UnixNano()
}

func GetInstance() *Logger {
	once.Do(func() {
		instance = &Logger{
			entries:    make([]string, 0),
			instanceID: idCounter,
		}
	})
	return instance
}

func (l *Logger) formatEntry(level, message string) string {
	return fmt.Sprintf("[%s] %s: %s",
		time.Now().Format("2006-01-02 15:04:05"),
		level,
		message,
	)
}

func (l *Logger) logInternal(level, message string) {
	l.mu.Lock()
	defer l.mu.Unlock()

	entry := l.formatEntry(level, message)
	l.entries = append(l.entries, entry)
	fmt.Println(entry)
}

func (l *Logger) Log(mensagem string) {
	l.logInternal(LevelLog, mensagem)
}

func (l *Logger) Info(mensagem string) {
	l.logInternal(LevelInfo, mensagem)
}

func (l *Logger) Warning(mensagem string) {
	l.logInternal(LevelWarning, mensagem)
}

func (l *Logger) Error(mensagem string) {
	l.logInternal(LevelError, mensagem)
}

func (l *Logger) InstanceID() int64 {
	return l.instanceID
}

func (l *Logger) SaveToFile(caminho string) error {
	l.mu.Lock()
	defer l.mu.Unlock()

	f, err := os.Create(caminho)
	if err != nil {
		return fmt.Errorf("criar arquivo: %w", err)
	}
	defer f.Close()

	for _, entry := range l.entries {
		if _, err := fmt.Fprintln(f, entry); err != nil {
			return fmt.Errorf("escrever log: %w", err)
		}
	}

	return nil
}

func (l *Logger) Entries() []string {
	l.mu.Lock()
	defer l.mu.Unlock()

	cp := make([]string, len(l.entries))
	copy(cp, l.entries)
	return cp
}
